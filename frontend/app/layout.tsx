export const metadata = {
    title: 'GSpot',
    description: 'Games market',
}

export default function RootLayout({ children }: { children: React.ReactNode }) {
    return (
        <html lang="ru">
            <body>{children}</body>
        </html>
    )
}
