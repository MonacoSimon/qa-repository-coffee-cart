class AddProduct {
    add(product) {
        cy.get(`[data-cy="${product}"]`).click();
    }
}

export default AddProduct;