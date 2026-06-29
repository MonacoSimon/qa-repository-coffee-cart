import HomePage from "../pages/HomePage"
import AddProduct from "../pages/AddProduct";

describe('pay hover', () => {
  const goHome = new HomePage();
  const add = new AddProduct();

  it('passes', () => {
    goHome.visit();
    cy.get('.router-link-active').should('be.visible')
    add.add('Espresso-Macchiato');

    cy.get('[data-test="checkout"]').trigger('mouseover')
    cy.contains('Espresso Macchiato').should('be.visible')
  })
})