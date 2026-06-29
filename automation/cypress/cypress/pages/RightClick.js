class Rightclick {
    rightClick(product) {
        cy.get(`[data-cy="${product}"]`).rightclick()
    }
}
export default Rightclick;