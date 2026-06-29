import HomePage from '../pages/HomePage'
import AddProduct from '../pages/AddProduct';

describe('shopping cart', () => {

  const home = new HomePage();
  const add = new AddProduct();

  it('passes', () => {
    home.visit();
    cy.wait(1000)
    cy.get('img').should('be.visible')
    add.add('Espresso-Macchiato')
    cy.get(':nth-child(2) > a').click()
    cy.get('ul[data-v-8965af83=""] > .list-item > :nth-child(1)').should('be.visible')
  })
})