use pyo3::{pyclass, pymethods, pymodule, types::PyModule, PyResult, Python};

#[pyclass]
pub struct Simulation {}
#[pymethods]
impl Simulation {
    #[new]
    pub fn new() -> Simulation {
        Simulation {}
    }

    pub fn add_species(&mut self, name: String, eats: Vec<String>) {
        println!("Species added: {name}! it eats {eats:?}");
        todo!()
    }

    pub fn get_frame(&self) -> Vec<Option<String>> {
        println!("Frame gotten!");
        todo!()
    }

    pub fn remove_species(&mut self, name: String) {
        println!("Tried to remove {name}!");
        todo!()
    }

    pub fn advance(&mut self) {
        println!("Advanced!");
        todo!()
    }
}

#[pymodule]
fn env_sim(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_class::<Simulation>()?;
    Ok(())
}
