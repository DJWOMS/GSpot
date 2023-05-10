import s from './page.module.css'

export default function Layout({
  children,
  password,
  profile,
}: {
  children: React.ReactNode
  password: React.ReactNode
  profile: React.ReactNode
}) {
  return (
    <div className={s.row}>
      {children}
      {profile}
      {password}
    </div>
  )
}
