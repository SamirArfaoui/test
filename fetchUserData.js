const TaskManager = () => {
    const tasks = [];

    const addTask = (taskName, priority = 'Normal') => {
        const task = { taskName, priority };
        tasks.push(task);
        return tasks;
    };

    return { tasks, addTask };
};

export default TaskManager;
