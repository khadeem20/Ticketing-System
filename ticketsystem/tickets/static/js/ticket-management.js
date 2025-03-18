document.addEventListener("DOMContentLoaded", function (){
    
    const ticketLinks = document.querySelectorAll(".open-ticket-modal");

    ticketLinks.forEach( link => {
        
        link.addEventListener('click', function(){
            document.getElementById("modalTitle").textContent= this.getAttribute("data-title");
            document.getElementById("modalPriority").textContent= this.getAttribute("data-priority");
            document.getElementById("modalStatus").textContent=this.getAttribute("data-status");
            document.getElementById("modalAssigned").textContent=this.getAttribute("data-assigned_to");
            document.getElementById("modalDate").textContent=this.getAttribute("data-created date");
            document.getElementById("modalDescription").textContent=this.getAttribute("data-description");
        });
    });
    
});