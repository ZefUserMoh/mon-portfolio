// douceurs-gourmandises/js/script.js
document.addEventListener('DOMContentLoaded', () => {
    // Mise à jour du compteur de panier global (clé dg_cart utilisée par les autres pages)
    const updateGlobalCount = () => {
        const navCount = document.getElementById('nav-cart-count');
        const panierCountElement = document.getElementById('panier-count') || navCount;
        
        if (panierCountElement) {
            const cart = JSON.parse(localStorage.getItem('dg_cart')) || [];
            const count = cart.reduce((acc, item) => acc + (item.qty || 0), 0);
            panierCountElement.textContent = count;
        }
    };

    updateGlobalCount();

    // Gestion de la soumission des formulaires (Contact, etc.)
    const contactForm = document.querySelector('section form');
    if (contactForm && !contactForm.id.includes('commande')) {
        contactForm.addEventListener('submit', (e) => {
            e.preventDefault();
            alert('Merci ! Votre demande a été reçue. Nous vous contacterons très prochainement.');
            contactForm.reset();
        });
    }
});
