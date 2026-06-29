import HomePage from "../pages/HomePage"
import Rightclick from "../pages/RightClick";

describe('test button add to cart', () => {
  const goHome = new HomePage();
  const rightClick = new Rightclick();

  it('passes', () => {
    goHome.visit();

    cy.get('.router-link-active').should('be.visible')

    rightClick.rightClick('Espresso-Macchiato');

    cy.get('[data-cy="add-to-cart-modal"]').should('be.visible')
    cy.get('[data-cy="add-to-cart-modal"]').contains('Yes').click()
    cy.get(':nth-child(2) > a').should('contain', 'cart (1)')
  })
})