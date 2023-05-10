import React from 'react'
import { fireEvent, render, screen, waitFor } from '@testing-library/react'
import { generateMockGameCardSimple } from 'features/games/mocks'
import Input from './SearchInput'

describe('Input component', () => {
  const mockOnChange = jest.fn()
  const mockResults = [...new Array(3)].map(() => generateMockGameCardSimple())

  afterEach(() => {
    jest.clearAllMocks()
  })

  it('renders a Combobox.Input element', () => {
    render(<Input onChange={mockOnChange} result={mockResults} />)
    const inputElement = screen.getByRole('combobox') as HTMLInputElement
    expect(inputElement).toBeVisible()
  })

  it('displays a list of options when the user types into the input', async () => {
    render(<Input onChange={mockOnChange} result={mockResults} />)
    const inputElement = screen.getByRole('combobox') as HTMLInputElement

    fireEvent.change(inputElement, { target: { value: mockResults[0].title } })

    const optionsElement = await screen.findByRole('listbox')
    waitFor(() => {
      expect(optionsElement).toBeVisible()
    })
  })

  it('calls the onChange function when the user types into the input', () => {
    render(<Input onChange={mockOnChange} result={mockResults} />)
    const inputElement = screen.getByRole('combobox') as HTMLInputElement

    fireEvent.change(inputElement, { target: { value: mockResults[0].title } })

    waitFor(() => {
      expect(mockOnChange).toHaveBeenCalledTimes(1)
      expect(mockOnChange).toHaveBeenCalledWith('Category')
    })
  })
})
