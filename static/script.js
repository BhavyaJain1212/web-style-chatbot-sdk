document.getElementById("urlForm").addEventListener("submit", async (event) => {
  event.preventDefault(); // Prevent form submission and page reload

  console.log("form submitted")

  // url as string
  const url = document.getElementById("urlInput").value
  console.log(url)

  try {
    const response = await fetch("/fetch-website-code", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        web_url: url
      })
    })

    const data = await response.json()
    console.log("Response:", data)

  } catch (error) {
    console.error("Network error:", error)
  }
});