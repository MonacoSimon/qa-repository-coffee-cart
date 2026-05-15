describe('template spec', () => {
  it('passes', () => {
    cy.visit('https://coffee-cart.app/')
    cy.get('.router-link-active').should('be.visible')
    cy.get(':nth-child(3) > a').click()
    cy.get('.container > :nth-child(3) > :nth-child(3)').should('contain', 'Desktop')
    cy.get('.container > :nth-child(1) > a').click()
  })
})