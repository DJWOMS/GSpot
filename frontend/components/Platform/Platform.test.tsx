import React from 'react'
import { render } from '@testing-library/react'
import Platform from './Platform'

describe('CardPlatform', () => {
  test('renders the "ps" platform', () => {
    const { container } = render(<Platform type="ps" />)
    expect(container.firstChild).toHaveClass('platform ps')
  })

  test('renders the "xbox" platform', () => {
    const { container } = render(<Platform type="xbox" />)
    expect(container.firstChild).toHaveClass('platform xbox')
  })

  test('renders the "win" platform', () => {
    const { container } = render(<Platform type="win" />)
    expect(container.firstChild).toHaveClass('platform win')
  })

  test('renders the "ap" platform', () => {
    const { container } = render(<Platform type="ap" />)
    expect(container.firstChild).toHaveClass('platform ap')
  })
})
