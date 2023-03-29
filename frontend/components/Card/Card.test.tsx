import React from 'react'
import { render } from '@testing-library/react'
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

    expect(getByText(props.title)).toBeInTheDocument()
    expect(getByText(`${props.currency}${props.price}`)).toBeInTheDocument()
    expect(getByText(`${props.currency}${props.sale}`)).toBeInTheDocument()
  })

  it('renders the card without a sale price', () => {
    const { getByText, queryByText } = render(<Card {...props} sale={undefined} />)

    expect(getByText(`${props.currency}${props.price}`)).toBeInTheDocument()
    expect(queryByText(`${props.currency}${props.sale}`)).toBeNull()
  })
})
