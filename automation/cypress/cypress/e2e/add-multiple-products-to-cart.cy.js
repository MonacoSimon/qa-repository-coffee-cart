import HomePage from "../pages/HomePage"
import AddProduct from "../pages/AddProduct";
import GoCart from '../pages/GoCart'

describe('Add products to the cart', () => {
  const goHome = new HomePage();
  const addProduct = new AddProduct();
  const goCart = new GoCart();

  it('passes', () => {
    goHome.visit();
    cy.get('.router-link-active').should('be.visible')

    addProduct.add('Espresso-Macchiato');
    addProduct.add('Americano');

    cy.get(':nth-child(2) > a').should('contain', 'cart (2)')

    goCart.goCart();

    cy.get('ul[data-v-8965af83=""] > .list-item > :nth-child(1)').should('contain', 'Espresso Macchiato')
    cy.get('ul[data-v-8965af83=""] > .list-item > :nth-child(1)').should('contain', 'Americano')
    cy.get('[data-test="checkout"]').should('contain', 'Total: $19.00')
  })
})