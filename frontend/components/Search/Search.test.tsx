import React from 'react'
import { fireEvent, render, waitFor } from '@testing-library/react'
import Search from './Search'

describe('Search component', () => {
  it('renders Search component without crashing', () => {
    render(<Search />)
  })

  it('can change search input', () => {
    const { getByPlaceholderText } = render(<Search />)
    const input = getByPlaceholderText('Я ищу...') as HTMLInputElement

    fireEvent.change(input, { target: { value: 'test' } })
    waitFor(() => {
      expect(input.value).toBe('test')
    })
  })

  it('can click search button', () => {
    const { getByRole } = render(<Search />)
    const button = getByRole('button', { name: '' })

    fireEvent.click(button)
  })

  it('hides options when input value is shorter than 3 characters', () => {
    const { getByPlaceholderText, queryByText } = render(<Search />)
    const input = getByPlaceholderText('Я ищу...') as HTMLInputElement

    fireEvent.change(input, { target: { value: 'te' } })

    waitFor(() => {
      expect(queryByText('Приключения')).toBeNull()
    })
  })
})
