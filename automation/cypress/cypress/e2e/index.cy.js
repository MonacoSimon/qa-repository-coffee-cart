import HomePage from "../pages/HomePage"

describe('test visibility of Home Page', () => {
  const goHome = new HomePage();

  it('passes', () => {
    goHome.visit();
    cy.get('.router-link-active').should('be.visible')
  })
})