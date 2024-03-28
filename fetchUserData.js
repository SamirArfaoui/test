export default fetchUserData = () => {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            resolve({ name: 'John', age:30, email:"john.doe@example.com" });
        }, 2000);
        reject('Failed to fetch data');
    });
}

const f = fetchUserData ();