import HomePage from "../pages/HomePage"
import AddProduct from "../pages/AddProduct";
import GoCart from "../pages/GoCart";

describe('activate discount section', () => {
  const goHome = new HomePage();
  const add = new AddProduct();
  const goCart = new GoCart();

  it('passes', () => {
    goHome.visit();
    cy.get('.router-link-active').should('be.visible')

    add.add('Espresso-Macchiato');
    add.add('Americano');
    add.add('Mocha');

    cy.get('.promo > span').should('contain', "It's your lucky day! Get an extra cup of Mocha for $4")
    cy.get('.yes').click()
    cy.get(':nth-child(2) > a').should('contain', 'cart (4)')
    goCart.goCart();
    cy.get('ul[data-v-8965af83=""] > .list-item > :nth-child(1)').should('contain', 'Espresso Macchiato')
    cy.get('ul[data-v-8965af83=""] > .list-item > :nth-child(1)').should('contain', 'Americano')
    cy.get('ul[data-v-8965af83=""] > .list-item > :nth-child(1)').should('contain', 'Mocha')
    cy.get('[data-test="checkout"]').should('contain', 'Total: $31.00')
  })
})