import React from 'react'
import { render, waitFor } from '@testing-library/react'
import { GameCardInterface } from 'features/games'
import Card from './Card'

describe('Card', () => {
  const props: GameCardInterface = {
    coverImg: 'https://example.com/cover.jpg',
    link: '/game',
    title: 'Example Game',
    sale: 10,
    currency: 'USD',
    price: 50,
  }

  it('renders the card with all props', () => {
    const { getByText } = render(<Card {...props} />)

    waitFor(() => {
      expect(getByText(props.title)).toBeVisible()
      expect(getByText(`${props.currency}${props.price}`)).toBeVisible()
      expect(getByText(`${props.currency}${props.sale}`)).toBeVisible()
    })
  })

  it('renders the card without a sale price', () => {
    const { getByText, queryByText } = render(<Card {...props} sale={undefined} />)

    expect(getByText(`${props.currency}${props.price}`)).toBeVisible()
    expect(queryByText(`${props.currency}${props.sale}`)).toBeNull()
  })
})
