describe('template spec', () => {
  it('passes', () => {
    cy.visit('https://coffee-cart.app/')
    cy.get('.router-link-active').should('be.visible')
    cy.get('[data-cy="Espresso-Macchiato"]').click()
    cy.get(':nth-child(2) > a').should('contain', 'cart (1)')
    cy.get(':nth-child(2) > a').click()
    cy.get('ul[data-v-8965af83=""] > .list-item > :nth-child(1)').should('contain', 'Espresso Macchiato')
  })
})