describe('template spec', () => {
  it('passes', () => {
    cy.visit('https://coffee-cart.app/')
    cy.get('.router-link-active').should('be.visible')
    cy.get('[data-cy="Espresso-Macchiato"]').click()
    cy.get('[data-test="checkout"]').trigger('mouseover')
    cy.contains('Espresso Macchiato').should('be.visible')
  })
})