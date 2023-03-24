import React from 'react'
import Breadcrumbs from './Breadcrumbs'

describe('<Breadcrumbs />', () => {
  it('renders', () => {
    // see: https://on.cypress.io/mounting-react
    cy.mount(<Breadcrumbs />)
  })
})
