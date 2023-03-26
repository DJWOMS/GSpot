import { render } from '@testing-library/react'
import CardBig from './CardBig'

describe('CardBig', () => {
  const props = {
    coverImg: 'test-image.jpg',
    badge: 'New',
    link: '/test',
    title: 'Test Game',
    price: 50,
    currency: '$',
  }

  it('should render correctly', () => {
    const { getByText, getByAltText } = render(<CardBig {...props} />)
    const titleElement = getByText('Test Game')
    const currencyElement = getByText('$', { exact: false })
    const priceElement = getByText('50', { exact: false })

    expect(getByAltText('')).toHaveAttribute('src', 'test-image.jpg')
    expect(currencyElement).toBeInTheDocument()
    expect(titleElement).toBeInTheDocument()
    expect(priceElement).toBeInTheDocument()
  })

  it('should render a sale price when given a sale prop', () => {
    const { getByText } = render(<CardBig {...props} sale={25} />)
    const salePriceElement = getByText('25', { exact: false })
    const regularPriceElement = getByText('50', { exact: false })

    expect(salePriceElement).toBeInTheDocument()
    expect(regularPriceElement.tagName).toBe('S')
  })

  it('should not render a badge when no badge prop is given', () => {
    const { queryByText } = render(<CardBig {...props} badge={undefined} />)
    const badgeElement = queryByText('New')

    expect(badgeElement).not.toBeInTheDocument()
  })

  it('should render with a "cardBig" class when given a big prop', () => {
    const { container } = render(<CardBig {...props} big />)
    const cardElement = container.querySelector('.cardBig')

    expect(cardElement).toBeInTheDocument()
  })
})
