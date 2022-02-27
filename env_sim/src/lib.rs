use std::collections::BTreeMap;

use pyo3::{pyclass, pymethods, pymodule, types::PyModule, PyResult, Python};
use rand::Rng;

#[pyclass]
pub struct Simulation {
    specieses: BTreeMap<String, Species>,
    data: Vec<Vec<Square>>,
    width: usize,
    height: usize,
    changes: BTreeMap<(usize, usize), Vec<Change>>,
}

#[derive(Debug, Clone)]
enum Square {
    Empty {
        converted_to: Option<String>,
        conversion_progress: usize,
    },
    Occupied(Organism),
}

#[derive(Debug, Clone, PartialEq, Eq)]
enum Change {
    Die,
    BecomeSpecies(String),
    ConversionProgress(usize),
    StartConverting(String),
    Bred,
    LoseHealth(usize),
    NotEat,
    Eat,
}

#[derive(Debug, Clone)]
struct Species {
    eats: Vec<String>,
    hardiness: usize,
    growth_speed: usize,
    breeding_age: usize,
}

impl Square {
    fn is_occupied(&self) -> bool {
        if let Square::Occupied(_) = self {
            true
        } else {
            false
        }
    }
    fn unwrap_organism(&self) -> &Organism {
        if let Square::Occupied(org) = self {
            org
        } else {
            panic!()
        }
    }
    fn unwrap_organism_mut(&mut self) -> &mut Organism {
        if let Square::Occupied(org) = self {
            org
        } else {
            panic!()
        }
    }
}

#[derive(Debug, Clone, Hash, PartialEq, Eq, PartialOrd, Ord)]
struct Organism {
    species: String,
    health: usize,
    age: usize,
    breeding_potential: usize,
    time_since_eaten: usize,
}

fn wrap_around(p1: isize, p2: usize) -> usize {
    if (p1.abs() as usize) < p2 {
        return (p2 as isize + p1) as usize;
    }
    if p1 > 0 {
        return (p1 as usize + p2) % p2;
    }
    return p2 - (p1 * -1) as usize;
}

impl Simulation {
    fn get_around_pos(&self, x: usize, y: usize) -> Vec<(usize, usize, &Square)> {
        let mut t = Vec::new();
        for dx in -1..=1 {
            for dy in -1..=1 {
                if dy != 0 && dx != 0 {
                    let square_x = wrap_around(dx, x);
                    let square_y = wrap_around(dy, y);
                    t.push((square_x, square_y, &self.data[square_x][square_y]))
                }
            }
        }
        t
    }

    fn resolve_changes(&mut self) {
        for ((x, y), changes) in self.changes.iter() {
            let pos = &mut self.data[*x][*y];
            for change in changes {
                match change {
                    Change::Die => {
                        *pos = Square::Empty {
                            converted_to: None,
                            conversion_progress: 0,
                        }
                    }
                    Change::BecomeSpecies(name) => {
                        let spec = self.specieses.get(name).unwrap();
                        *pos = Square::Occupied(Organism {
                            species: name.clone(),
                            health: spec.hardiness,
                            age: 0,
                            breeding_potential: 0,
                            time_since_eaten: 0,
                        });
                    }
                    Change::ConversionProgress(more_progress) => match pos {
                        Square::Empty {
                            converted_to: _,
                            conversion_progress: prog,
                        } => *prog += more_progress,
                        _ => panic!(),
                    },
                    Change::StartConverting(name) => match pos {
                        Square::Empty {
                            converted_to: s,
                            conversion_progress: _,
                        } => *s = Some(name.clone()),
                        _ => panic!(),
                    },
                    Change::Bred => pos.unwrap_organism_mut().breeding_potential = 0,
                    Change::LoseHealth(h) => {
                        pos.unwrap_organism_mut().health =
                            pos.unwrap_organism_mut().health.saturating_sub(*h)
                    }
                    Change::NotEat => {
                        pos.unwrap_organism_mut().time_since_eaten =
                            pos.unwrap_organism_mut().time_since_eaten.saturating_sub(1)
                    }
                    Change::Eat => pos.unwrap_organism_mut().time_since_eaten = 0,
                }
            }
            if let Square::Occupied(org) = pos {
                org.breeding_potential += self.specieses.get(&org.species).unwrap().growth_speed;
            }
        }
    }
}

#[pymethods]
impl Simulation {
    #[new]
    pub fn new(width: Option<usize>, height: Option<usize>) -> Simulation {
        let width = width.unwrap_or(300);
        let height = height.unwrap_or(300);
        Simulation {
            specieses: BTreeMap::new(),
            data: vec![
                vec![
                    Square::Empty {
                        converted_to: None,
                        conversion_progress: 0
                    };
                    height
                ];
                width
            ],
            width,
            height,
            changes: BTreeMap::new(),
        }
    }
    pub fn add_species(
        &mut self,
        name: String,
        eats: Vec<String>,
        hardiness: Option<usize>,
        growth_speed: Option<usize>,
        breeding_age: Option<usize>,
    ) {
        if !self.specieses.contains_key(&name) {
            let spec = Species {
                eats,
                hardiness: hardiness.unwrap_or(5),
                growth_speed: growth_speed.unwrap_or(5),
                breeding_age: breeding_age.unwrap_or(5),
            };
            self.specieses.insert(name.clone(), spec);
            if eats.contains(&"sunlight".to_string()) {
                for t in &mut self.data {
                    for a in t.iter_mut() {
                        if !a.is_occupied() {
                            a = Organism {
                                species: name.clone(),
                                health: hardiness.unwrap_or(20),
                                age: 0,
                                breeding_potential: 0,
                                time_since_eaten: 0,
                            }
                        }
                    }
                }
            } else {
                for _ in 0..5 {
                    let rand = rand::thread_rng();
                    self.data[rand.gen_range(0..self.width)][rand.gen_range(0..self.height)] =
                        Square::Occupied(Organism {
                            species: name.clone(),
                            health: hardiness.unwrap_or(20),
                            age: 0,
                            breeding_potential: 0,
                            time_since_eaten: 0,
                        })
                }
            }
        }
    }

    pub fn get_frame(&self) -> (Vec<Option<String>>, usize, usize) {
        let mut disp = Vec::with_capacity(self.width * self.height);
        for t in &self.data {
            disp.extend(t.clone())
        }
        let disp = disp
            .into_iter()
            .map(|x| match x {
                Square::Occupied(org) => Some(org.species),
                _ => None,
            })
            .collect();
        (disp, self.width, self.height)
    }

    pub fn remove_species(&mut self, name: String) {
        if self.specieses.contains_key(&name) {
            self.specieses.remove(&name);
        }
        for x in 0..self.width {
            for y in 0..self.height {
                let t = &mut self.data[x][y];
                if let Square::Occupied(org) = t {
                    if org.species == name {
                        *t = Square::Empty {
                            converted_to: None,
                            conversion_progress: 0,
                        }
                    }
                }
            }
        }
    }

    pub fn advance(&mut self) {
        self.changes = BTreeMap::new();
        for x in 0..self.width {
            for y in 0..self.height {
                let square = &self.data[x][y];
                let around = self.get_around_pos(x, y);
                let not_empty = around
                    .into_iter()
                    .filter(|x| Square::is_occupied(&x.2))
                    .collect::<Vec<_>>();
                match square {
                    Square::Occupied(org) => {
                        if org.health == 0 {
                            self.changes.entry((x, y)).or_default().push(Change::Die);
                        } else {
                            if !not_empty.is_empty() {
                                let eats = &self.specieses.get(&org.species).unwrap().eats;
                                if eats.contains(&"sunlight".to_string()) {
                                    self.changes.entry((x, y)).or_default().push(Change::Eat)
                                } else {
                                    let mut ate = false;
                                    'eating: for (other_x, other_y, other_square) in not_empty {
                                        let other_org = other_square.unwrap_organism();
                                        if eats.contains(&other_org.species) {
                                            self.changes
                                                .entry((other_x, other_y))
                                                .or_default()
                                                .push(Change::LoseHealth(5));
                                            self.changes
                                                .entry((x, y))
                                                .or_default()
                                                .push(Change::Eat);
                                            ate = true;
                                            break 'eating;
                                        }
                                    }
                                    if !ate {
                                        if org.time_since_eaten > 5 {
                                            self.changes
                                                .entry((x, y))
                                                .or_default()
                                                .push(Change::Die);
                                        } else {
                                            self.changes
                                                .entry((x, y))
                                                .or_default()
                                                .push(Change::NotEat)
                                        }
                                    }
                                }
                            }
                        }
                    }
                    Square::Empty {
                        converted_to: None,
                        conversion_progress: _,
                    } => {
                        if !not_empty.is_empty() {
                            let mut values = BTreeMap::new();
                            for (thing_x, thing_y, thing) in not_empty {
                                let thing = thing.unwrap_organism();
                                if thing.age
                                    > self.specieses.get(&thing.species).unwrap().breeding_age
                                    && (self.changes.get(&(thing_x, thing_y)).is_none()
                                        || !self
                                            .changes
                                            .get(&(thing_x, thing_y))
                                            .unwrap()
                                            .contains(&Change::Bred))
                                    && thing.breeding_potential > 20
                                {
                                    *values.entry((thing_x, thing_y, thing)).or_insert(0) +=
                                        thing.breeding_potential;
                                }
                            }
                            let mut highest = 0;
                            let mut breeder = None;
                            for (details, score) in values {
                                if score > highest {
                                    highest = score;
                                    breeder = Some(details);
                                }
                            }
                            if let Some((pos_x, pos_y, breeder)) = breeder {
                                let spec = breeder.species.clone();
                                self.changes
                                    .entry((pos_x, pos_y))
                                    .or_insert(Vec::new())
                                    .push(Change::Bred);
                                self.changes
                                    .entry((x, y))
                                    .or_insert(Vec::new())
                                    .extend_from_slice(&[
                                        Change::StartConverting(spec),
                                        Change::ConversionProgress(highest),
                                    ]);
                            }
                        }
                    }
                    Square::Empty {
                        converted_to: Some(species_name),
                        conversion_progress: prog,
                    } => {
                        if *prog > 5 {
                            self.changes
                                .entry((x, y))
                                .or_insert(Vec::new())
                                .push(Change::BecomeSpecies(species_name.to_string()));
                        } else if !not_empty.is_empty() {
                            let mut values = BTreeMap::new();
                            for (thing_x, thing_y, thing) in not_empty {
                                let thing = thing.unwrap_organism();
                                if thing.age
                                    > self.specieses.get(&thing.species).unwrap().breeding_age
                                    && (self.changes.get(&(thing_x, thing_y)).is_none()
                                        || !self
                                            .changes
                                            .get(&(thing_x, thing_y))
                                            .unwrap()
                                            .contains(&Change::Bred))
                                    && thing.breeding_potential > 20
                                    && &thing.species == species_name
                                {
                                    *values.entry((thing_x, thing_y, thing)).or_insert(0) +=
                                        thing.breeding_potential;
                                }
                            }
                            let mut highest = 0;
                            let mut breeder = None;
                            for (details, score) in values {
                                if score > highest {
                                    highest = score;
                                    breeder = Some(details);
                                }
                            }
                            if let Some((pos_x, pos_y, _)) = breeder {
                                self.changes
                                    .entry((pos_x, pos_y))
                                    .or_insert(Vec::new())
                                    .push(Change::Bred);
                                self.changes
                                    .entry((x, y))
                                    .or_insert(Vec::new())
                                    .extend_from_slice(&[Change::ConversionProgress(highest)]);
                            }
                        }
                    }
                }
            }
        }
        self.resolve_changes();
    }
}

#[pymodule]
fn env_sim(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_class::<Simulation>()?;
    Ok(())
}
