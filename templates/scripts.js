document
  .getElementById("gatePassForm")
  .addEventListener("submit", function (event) {
    event.preventDefault(); // Form ko reload hone se roko

    const name = document.getElementById("name").value;
    const date = document.getElementById("date").value;
    const reason = document.getElementById("reason").value;
    const entryTime = document.getElementById("entryTime").value;
    const exitTime = document.getElementById("exitTime").value;

    if (name && date && reason && entryTime) {
      alert("Gate pass submitted successfully!");
      console.log({
        name: name,
        date: date,
        reason: reason,
        entryTime: entryTime,
        exitTime: exitTime || "Not provided",
      });
      // Tum yaha form ka data backend pe bhejne ka code bhi add kar sakte ho
    } else {
      alert("Please fill in all required fields.");
    }
  });
