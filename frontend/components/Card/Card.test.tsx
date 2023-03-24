import { render } from '@testing-library/react'
import Card from './Card'

describe('Card', () => {
  const props = {
    coverImg: 'https://example.com/cover.jpg',
    badge: 'New',
    link: '/game',
    title: 'Example Game',
    sale: 10,
    price: 50,
  }

  it('renders the card with all props', () => {
    const { getByText, getByAltText } = render(<Card {...props} />)

    expect(getByAltText('')).toHaveAttribute('src', props.coverImg)
    expect(getByText(props.badge)).toBeInTheDocument()
    expect(getByText(props.title)).toBeInTheDocument()
    expect(getByText(props.price)).toBeInTheDocument()
    expect(getByText(props.sale)).toBeInTheDocument()
  })

  it('renders the card without a sale price', () => {
    const { getByText, queryByText } = render(<Card {...props} sale={undefined} />)

    expect(getByText(props.price)).toBeInTheDocument()
    expect(queryByText(props.sale)).toBeNull()
  })

  it('renders the card without a badge', () => {
    const { queryByText } = render(<Card {...props} badge={undefined} />)

    expect(queryByText(props.badge)).not.toBeInTheDocument()
  })
})
