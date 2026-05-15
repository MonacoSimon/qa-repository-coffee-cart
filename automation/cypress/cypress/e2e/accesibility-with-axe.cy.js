import 'cypress-axe';

describe('Accesibilidad - Home', () => {

  it('no debería tener errores críticos', () => {

    cy.intercept('GET', '/list.json').as('coffeeList')

    cy.visit('https://coffee-cart.app/')

    cy.wait('@coffeeList')

    cy.contains('Espresso')
      .should('be.visible')

    cy.injectAxe()

    cy.checkA11y(null, {
      includedImpacts: ['critical', 'serious']
    })

  })

})