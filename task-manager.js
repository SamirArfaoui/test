function fetchUserData() {
  return new Promise((resolve, reject) => {
    const random = Math.random();
    setTimeout(() => {
      if (random < 0.5) {
        resolve({ name: "John Doe", age: 30, email: "john.doe@example.com" });
      } else {
        reject("Failed to fetch data");
      }
    }, 2000);
  });
}

fetchUserData()
  .then((user) => {
    console.log(`Name: ${user.name}`);
    console.log(`Email: ${user.email}`);
  })
  .catch((error) => {
    console.log("Error fetching data");
  });