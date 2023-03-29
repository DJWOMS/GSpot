import { render } from '@testing-library/react'
import Settings from './page'

describe('ProfileItem', () => {
  it('renders ProfileItem with items', () => {
    const { getByText } = render(<Settings />)

    expect(getByText('Ник')).toBeInTheDocument()
    expect(getByText('Email')).toBeInTheDocument()
    expect(getByText('Имя')).toBeInTheDocument()
    expect(getByText('Фaмилия')).toBeInTheDocument()
    expect(getByText('Старый пароль')).toBeInTheDocument()
    expect(getByText('Новый пароль')).toBeInTheDocument()
    expect(getByText('Подтвердить Новый пароль')).toBeInTheDocument()
    expect(getByText('Выбери опции')).toBeInTheDocument()
  })
})
