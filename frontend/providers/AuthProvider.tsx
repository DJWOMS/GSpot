'use client'

import { createContext, FC, ReactNode, useCallback, useState } from 'react'
import { fetchServerSide } from 'lib/fetchServerSide'

interface Props {
  children: ReactNode
}

interface IContext {
  authenticated: boolean
  setAuthenticated: (value: boolean) => void
  authenticate: () => Promise<void>
  refresh: () => Promise<void>
  checkAuth: () => Promise<boolean>
}

export const AuthContext = createContext<IContext>({
  authenticated: false,
  setAuthenticated: () => {},
  authenticate: async () => {},
  refresh: async () => {},
  checkAuth: async () => false,
})

interface TokenResponse {
  refresh_token: string
  access_token: string
}

export const AuthProvider: FC<Props> = ({ children }) => {
  const [authenticated, setAuthenticated] = useState(false)

  const authenticate = useCallback(async () => {
    try {
      const data = await fetchServerSide<TokenResponse>({
        path: '/mocks/auth/access',
        body: JSON.stringify({ username: 'test', password: 'test' }),
        method: 'POST',
      })
      saveTokens(data?.access_token, data?.refresh_token)
    } catch {
      try {
        await refresh()
      } catch {
        setAuthenticated(false)
      }
    }
    setAuthenticated(true)
  }, [])

  const refresh = useCallback(async () => {
    const currentRefresh = currentTokens().refreshToken
    if (currentRefresh) {
      const data = await fetchServerSide<TokenResponse>({
        path: '/mocks/auth/refresh',
        method: 'POST',
        body: JSON.stringify({ refresh_token: currentTokens().refreshToken }),
      })
      saveTokens(data?.access_token, data?.refresh_token)
    }
  }, [])

  const checkAuth = useCallback(async () => {
    const currentAccess = currentTokens().accessToken
    if (currentAccess) {
      try {
        await fetchServerSide({
          path: '/mocks/auth/check',
          headers: {
            access_token: currentTokens().accessToken,
          },
        })
        return true
      } catch {
        return false
      }
    }
    return false
  }, [])

  const saveTokens = useCallback((accessToken?: string, refreshToken?: string) => {
    if (accessToken) {
      localStorage.setItem('access_token', accessToken)
    }
    if (refreshToken) {
      localStorage.setItem('refresh_token', refreshToken)
    }
  }, [])

  const currentTokens = useCallback(() => {
    const accessToken = localStorage.getItem('access_token') ?? ''
    const refreshToken = localStorage.getItem('refresh_token') ?? ''
    return {
      accessToken,
      refreshToken,
    }
  }, [])

  return (
    <AuthContext.Provider
      value={{
        authenticated,
        setAuthenticated,
        checkAuth,
        authenticate,
        refresh,
      }}
    >
      {children}
    </AuthContext.Provider>
  )
}
