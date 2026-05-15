describe('template spec', () => {
  it('passes', () => {
    cy.visit('https://coffee-cart.app/')
    cy.get('.router-link-active').should('be.visible')
    cy.get('[data-cy="Espresso-Macchiato"]').rightclick()
    cy.get('[data-cy="add-to-cart-modal"]').should('be.visible')
    cy.get('[data-cy="add-to-cart-modal"]').contains('Yes').click()
    cy.get(':nth-child(2) > a').should('contain', 'cart (1)')
  })
})