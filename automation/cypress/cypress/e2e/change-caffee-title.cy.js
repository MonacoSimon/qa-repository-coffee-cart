import HomePage from "../pages/HomePage"

describe('change product name', () => {
  const goHome = new HomePage();

  it('passes', () => {
    goHome.visit();

    cy.get('.router-link-active').should('be.visible')
    cy.get(':nth-child(2) > h4').should('be.visible')
    cy.get(':nth-child(2) > h4').dblclick()
    cy.contains('浓缩玛奇朵').should('be.visible')
  })
})