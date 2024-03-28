export default TaskManager() => {
    this.tasks = [];
  
    const self = this;
    this.addTask = (taskName, priority = 'Normal') => {
      const task = { taskName, priority };
      self.tasks.push(task);
      return self.tasks;
    };
  }
  