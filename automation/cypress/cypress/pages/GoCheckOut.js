class GoCheckOut {
    goCheckOut() {
        cy.get('[data-test="checkout"]').click()
    }
}
export default GoCheckOut;