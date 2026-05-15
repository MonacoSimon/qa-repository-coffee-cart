describe('template spec', () => {
  it('passes', () => {
    cy.visit('https://coffee-cart.app/?ad=1')
    cy.wait(1000)
    cy.get('img').should('be.visible')
    cy.get('[data-cy="Espresso-Macchiato"]').click()
    cy.get(':nth-child(2) > a').click()
  })
})