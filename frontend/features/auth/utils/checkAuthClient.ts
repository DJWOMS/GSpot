const doesHttpOnlyCookieExist = (cookieName: string) => {
  const d = new Date()
  d.setTime(d.getTime() + 1000)
  const expires = 'expires=' + d.toUTCString()

  document.cookie = cookieName + '=new_value;path=/;' + expires
  return document.cookie.indexOf(cookieName + '=') == -1
}

const checkAuthClient = async (): Promise<boolean> => {
  if (doesHttpOnlyCookieExist('access_token')) {
    return true
  }

  if (doesHttpOnlyCookieExist('refresh_token')) {
    try {
      await fetch('/auth/refresh', {
        method: 'POST',
        credentials: 'include',
      })
      return true
    } catch {
      return false
    }
  }
  return false
}

export default checkAuthClient
