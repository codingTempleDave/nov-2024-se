async function postData() {
  const userPost = await fetch("https://jsonplaceholder.typicode.com/posts",{
    method: "POST",    
    // this is the equivalent of body raw json from postman
    // we are giving a JSON string in the body to the API to process
    // jsonplaceholder will return the data we gave it as JSON
    body: JSON.stringify({
      title: "Why hello there",
      body: "Obi Wan speaks",
      userId: 2
    }),
    headers: {
      "Content-Type": "application/json"
    }
  });

  // converts JSON response string back into an object
  let response = userPost.json();
  return response;
}


async function startCall() {
  const serverResponse = await postData();

  document.getElementById("userInfo").innerHTML = `${serverResponse.title}<br>
                                                    ${serverResponse.body}<br>
                                                    ${serverResponse.userId}`;
  console.log(serverResponse);
}

startCall();