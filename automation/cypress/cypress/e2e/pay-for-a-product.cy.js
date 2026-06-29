import HomePage from "../pages/HomePage"
import AddProduct from '../pages/AddProduct'
import GoCart from '../pages/GoCart'
import GoCheckOut from "../pages/GoCheckOut"
import FillCheckoutData from "../pages/FillCheckoutData"

describe('pay for a prooduct', () => {
  const goHome = new HomePage();
  const add = new AddProduct();
  const goCart = new GoCart();
  const goCheckOut = new GoCheckOut();
  const fill = new FillCheckoutData();

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

    goCheckOut.goCheckOut();

    cy.get('h1').should('be.visible').should('contain', 'Payment details')

    fill.fillData('Simon', 'simonmonaco86@gmail.com')

    cy.get('.snackbar').should('be.visible')
  })
})