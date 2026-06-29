import HomePage from "../pages/HomePage"

describe('verify button github', () => {
  const goHome = new HomePage();

  it('passes', () => {
    goHome.visit();
    cy.get('.router-link-active').should('be.visible')
    cy.get(':nth-child(3) > a').click()
    cy.get('.container > :nth-child(3) > :nth-child(3)').should('contain', 'Desktop')
    cy.get('.container > :nth-child(1) > a').click()
  })
})