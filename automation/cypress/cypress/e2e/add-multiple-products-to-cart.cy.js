describe('template spec', () => {
  it('passes', () => {
    cy.visit('https://coffee-cart.app/')
    cy.get('.router-link-active').should('be.visible')
    cy.get('[data-cy="Espresso-Macchiato"]').click()
    cy.get('[data-cy="Americano"]').click()
    cy.get(':nth-child(2) > a').should('contain', 'cart (2)')
    cy.get(':nth-child(2) > a').click()
    cy.get('ul[data-v-8965af83=""] > .list-item > :nth-child(1)').should('contain', 'Espresso Macchiato')
    cy.get('ul[data-v-8965af83=""] > .list-item > :nth-child(1)').should('contain', 'Americano')
    cy.get('[data-test="checkout"]').should('contain', 'Total: $19.00')
  })
})