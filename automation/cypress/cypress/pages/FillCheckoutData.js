class FillCheckoutData {
    fillData(name, email) {
        cy.get('[name="name"]').type(name)
        cy.get('[name="email"]').type(email)
        cy.get('[name="promotion"]').click()
        cy.get('#submit-payment').click()
    }
}
export default FillCheckoutData;