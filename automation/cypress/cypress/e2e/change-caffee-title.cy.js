describe('template spec', () => {
  it('passes', () => {
    cy.visit('https://coffee-cart.app/')
    cy.get('.router-link-active').should('be.visible')
    cy.get(':nth-child(2) > h4').should('be.visible')
    cy.get(':nth-child(2) > h4').dblclick()
    cy.contains('浓缩玛奇朵').should('be.visible')
  })
})