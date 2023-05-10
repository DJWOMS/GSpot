import React from 'react'
import { render, waitFor } from '@testing-library/react'
import type { GameCardInterface } from 'features/games/types'
import GameCard from './GameCard'

describe('Card', () => {
  const props: GameCardInterface = {
    coverImg: 'https://example.com/cover.jpg',
    link: '/game',
    title: 'Example Game',
    sale: 10,
    currency: 'USD',
    price: 50,
    badge: 'New',
    platforms: [
      {
        type: 'ap',
      },
    ],
  }

  it('renders the card with all props', () => {
    const { getByText } = render(<GameCard {...props} />)

    waitFor(() => {
      expect(getByText(props.title)).toBeVisible()
      expect(getByText(`${props.currency}${props.price}`)).toBeVisible()
      expect(getByText(`${props.currency}${props.sale}`)).toBeVisible()
    })
  })

  it('renders the card without a sale price', () => {
    const { getByText, queryByText } = render(<GameCard {...props} sale={undefined} />)

    expect(getByText(`${props.currency}${props.price}`)).toBeVisible()
    expect(queryByText(`${props.currency}${props.sale}`)).toBeNull()
  })
})
