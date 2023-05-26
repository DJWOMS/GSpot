import { render } from '@testing-library/react'
import type { GameCardInterface } from 'features/games/types'
import { GameCardBig } from './GameCardBig'

describe('GameCardBig', () => {
  const props: GameCardInterface = {
    coverImg: 'https://example.com/cover.jpg',
    badge: 'New',
    link: '/test',
    title: 'Test Game',
    price: 50,
    currency: 'RUB',
    platforms: [
      {
        type: 'ap',
      },
    ],
  }

  it('should render correctly', () => {
    const { getByText } = render(<GameCardBig {...props} />)
    const titleElement = getByText('Test Game')
    const currencyElement = getByText('RUB', { exact: false })
    const priceElement = getByText('50', { exact: false })

    expect(currencyElement).toBeVisible()
    expect(titleElement).toBeVisible()
    expect(priceElement).toBeVisible()
  })

  it('should render a sale price when given a sale prop', () => {
    const { getByText } = render(<GameCardBig {...props} sale={25} />)
    const salePriceElement = getByText('25', { exact: false })
    const regularPriceElement = getByText('50', { exact: false })

    expect(salePriceElement).toBeVisible()
    expect(regularPriceElement.tagName).toBe('S')
  })

  it('should not render a badge when no badge prop is given', () => {
    const { queryByText } = render(<GameCardBig {...props} badge={undefined} />)
    const badgeElement = queryByText('New')

    expect(badgeElement).not.toBeInTheDocument()
  })

  it('should render with a "cardBig" class when given a big prop', () => {
    const { container } = render(<GameCardBig {...props} />)
    const cardElement = container.querySelector('.cardBig')

    expect(cardElement).toBeVisible()
  })
})
