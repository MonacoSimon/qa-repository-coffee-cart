import HomePage from "../pages/HomePage"
import AddProduct from "../pages/AddProduct";
import GoCart from "../pages/GoCart";

describe('remove a product from the cart', () => {
  const goHome = new HomePage();
  const add = new AddProduct();
  const goCart = new GoCart();

  it('passes', () => {
    goHome.visit();

    cy.get('.router-link-active').should('be.visible')
    add.add('Espresso-Macchiato');

    add.add('Americano');

    cy.get(':nth-child(2) > a').should('contain', 'cart (2)')
    cy.get(':nth-child(2) > a').click()
    cy.get('ul[data-v-8965af83=""] > .list-item > :nth-child(1)').should('contain', 'Espresso Macchiato')
    cy.get('ul[data-v-8965af83=""] > .list-item > :nth-child(1)').should('contain', 'Americano')
    cy.get('[data-test="checkout"]').should('contain', 'Total: $19.00')
    cy.get(':nth-child(2) > .unit-controller > [aria-label="Remove one Americano"]').click()
    cy.get(':nth-child(2) > a').should('contain', 'cart (1)')
    goCart.goCart();

    cy.get('ul[data-v-8965af83=""] > .list-item > :nth-child(1)').should('contain', 'Espresso Macchiato')
    cy.get('[data-test="checkout"]').should('contain', 'Total: $12.00')
  })
})