import { render } from '@testing-library/react'
import Breadcrumbs from './Breadcrumbs'

describe('Breadcrumbs', () => {
  const items = [{ name: 'Page 1', link: '/page1' }, { name: 'Page 2', link: '/page2' }, { name: 'Page 3' }]

  it('renders breadcrumbs with items', () => {
    const { getByText } = render(<Breadcrumbs items={items} />)

    expect(getByText('Главная')).toBeVisible()
    expect(getByText('Page 1')).toBeVisible()
    expect(getByText('Page 2')).toBeVisible()
    expect(getByText('Page 3')).toBeVisible()
  })

  it('renders breadcrumbs without items', () => {
    const { getByText } = render(<Breadcrumbs items={[]} />)

    expect(getByText('Главная')).toBeVisible()
  })

  it('renders last breadcrumb as active', () => {
    const { getByText } = render(<Breadcrumbs items={items} />)

    expect(getByText('Page 1')).not.toHaveClass('breadcrumbActive')
    expect(getByText('Page 2')).not.toHaveClass('breadcrumbActive')
    expect(getByText('Page 3')).toHaveClass('breadcrumbActive')
  })
})
