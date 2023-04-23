import Head from 'next/head'

export default function BaseHead({ 
  title = "Slide Maker", 
  description = "Construa slides para liturgia com facilidade",
  children 
}) {
  return (
    <Head>
      <title>{title}</title>
      <meta name="description" content={description} />
      <meta name="viewport" content="width=device-width, initial-scale=1" />
      <link rel="icon" href="/favicon.ico" />
      {children}
    </Head>
  )
}