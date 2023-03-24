import { render } from '@testing-library/react'
import Card from './Card'

describe('Card', () => {
  const props = {
    coverImg: 'https://example.com/cover.jpg',
    link: '/game',
    title: 'Example Game',
    sale: 10,
    currency: '$',
    price: 50,
  }

  it('renders the card with all props', () => {
    const { getByText, getByAltText } = render(<Card {...props} />)

    expect(getByAltText('')).toHaveAttribute('src', props.coverImg)
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
