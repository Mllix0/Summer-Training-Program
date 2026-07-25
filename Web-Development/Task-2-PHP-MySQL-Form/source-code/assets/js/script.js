const toggleButtons = document.querySelectorAll(".toggle-btn");

toggleButtons.forEach((button) => {
  button.addEventListener("click", async () => {
    const recordId = button.getAttribute("data-id");

    const formData = new FormData();
    formData.append("id", recordId);

    try {
      const response = await fetch("toggle_status.php", {
        method: "POST",
        body: formData
      });

      const result = await response.json();

      if (result.success) {
        const statusBadge = document.getElementById(`status-${recordId}`);

        statusBadge.textContent = result.newStatus;
        statusBadge.classList.remove("status-0", "status-1");
        statusBadge.classList.add(`status-${result.newStatus}`);
      } else {
        alert("Could not update status.");
      }

    } catch (error) {
      alert("Something went wrong while updating the status.");
      console.error(error);
    }
  });
});