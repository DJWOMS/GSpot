import { fireEvent, render, screen } from '@testing-library/react'
import Search from './Search'
import Input from './SearchInput'

describe('Search component', () => {
  it('renders Search component without crashing', () => {
    render(<Search />)
  })

  it('can change search input', () => {
    const { getByPlaceholderText } = render(<Search />)
    const input = getByPlaceholderText('Я ищу...')
    fireEvent.change(input, { target: { value: 'test' } })
    // eslint-disable-next-line @typescript-eslint/ban-ts-comment
    // @ts-ignore
    expect(input.value).toBe('test')
  })

  it('can click search button', () => {
    const { getByRole } = render(<Search />)
    const button = getByRole('button', { name: '' })
    fireEvent.click(button)
  })

  it('hides options when input value is shorter than 3 characters', () => {
    const { getByPlaceholderText, queryByText } = render(<Search />)
    const input = getByPlaceholderText('Я ищу...')
    fireEvent.change(input, { target: { value: 'te' } })
    expect(queryByText('Приключения')).toBeNull()
  })
})

describe('Input component', () => {
  const mockOnChange = jest.fn()
  const mockResults = [
    { id: 1, name: 'Category 1' },
    { id: 2, name: 'Category 2' },
  ]

  afterEach(() => {
    jest.clearAllMocks()
  })

  it('renders a Combobox.Input element', () => {
    render(<Input onChange={mockOnChange} result={mockResults} />)
    const inputElement = screen.getByRole('combobox')
    expect(inputElement).toBeInTheDocument()
  })

  it('displays a list of options when the user types into the input', async () => {
    render(<Input onChange={mockOnChange} result={mockResults} />)
    const inputElement = screen.getByRole('combobox')

    fireEvent.change(inputElement, { target: { value: 'C' } })

    const optionsElement = await screen.findByRole('listbox')
    expect(optionsElement).toBeInTheDocument()
  })

  it('calls the onChange function when the user types into the input', () => {
    render(<Input onChange={mockOnChange} result={mockResults} />)
    const inputElement = screen.getByRole('combobox')

    fireEvent.change(inputElement, { target: { value: 'Category' } })
    expect(mockOnChange).toHaveBeenCalledTimes(1)
    expect(mockOnChange).toHaveBeenCalledWith('Category')
  })
})
