class Bayes:
    """
    A class able to calculate posterior probabilities when given
    the priors, likelihood function, and possible observations.
    """

    def __init__(self, hypothesis: list[str], priors: list[float], observations: list[str], likelihood: list[list[float]]):
        """
        Initializes the Bayes class with the given parameters.
        Arguments:
            hypothesis: A list[str] of possible hypothesis.
            priors: A list[foat] of prior probabilities.
            observations: A list[str] of possible observations.
            likelihood: A list[list[float]] of likelihoods.
        """
        self.hypothesis = hypothesis
        self.priors = priors
        self.observations = observations
        self.likelihoods = likelihood

    def likelihood(self, observation: str, hypothesis: str):
        """
        Returns the likelihood of an observation given a hypothesis.
        Arguments:
            observation: String representing the observation.
            hypothesis: String representing the hypothesis.
        """
        observation_index = self.observations.index(observation)
        hypothesis_index = self.hypothesis.index(hypothesis)
        return self.likelihoods[hypothesis_index][observation_index]
    
    def norm_constant(self, observation: str):
        """
        Takes as input an observation and returns the normalization constant.
        Arguments:
            observation: String representing the observation.
        """ 
        norm_constant = 0
        for i in range(len(self.hypothesis)):
            norm_constant += self.likelihood(observation, self.hypothesis[i]) * self.priors[i]
        return norm_constant
    
    def single_posterior_update(self, observation: str, priors: list[float]):
        """
        Takes as input an observation and priors and returns the posterior probabilities.
        Arguments:
            observation: String representing the observation.
            priors: list[float] representing the priors.
        """
        self.priors = priors
        posterior = []
        norm_constant = self.norm_constant(observation)
        for i in range(len(self.hypothesis)):
            posterior.append((self.likelihood(observation, self.hypothesis[i]) * self.priors[i]) / norm_constant)
        return posterior
    
    def compute_posterior(self, observations: list[str]):
        """
        Takes as input a list of observations and returns the posterior probabilities.
        """
        posterior = self.priors
        for observation in observations:
            posterior = self.single_posterior_update(observation, posterior)
        return posterior
    

if __name__ == '__main__':

    ### EXERCICE 2 ###

    hypos = ["Bowl1", "Bowl2"]
    priors = [0.5, 0.5]
    obs = ["chocolate", "vanilla"]
    # e.g. likelihood[0][1] corresponds to the likehood of Bowl1 and vanilla, or 35/50
    likelihood = [[15/50, 35/50], [30/50, 20/50]]
    b = Bayes(hypos, priors, obs, likelihood)

    # l = b.likelihood("chocolate", "Bowl1")
    # print("likelihood(chocolate, Bowl1) = %s " % l)
    # n_c = b.norm_constant("chocolate")
    # print("normalizing constant for chocolate: %s" % n_c)
    p_1 = b.single_posterior_update("chocolate", [0.5, 0.5])
    print("chocolate - posterior: %s" % p_1)
    p_2 = b.compute_posterior(["chocolate", "vanilla"])
    # print("chocolate, vanilla - posterior: %s" % p_2)

    ### EXERCICE 3 ###
    # hypos = ["begginer", "intermediate", "advanced", "expert"]
    # obs = ["yellow", "red", "blue", "black", "white"]
    # likelihood = [[0.05, 0.1, 0.4, 0.25, 0.2],[0.1, 0.2, 0.4, 0.2, 0.1],[0.2, 0.4, 0.25, 0.1, 0.05],[0.3, 0.5, 0.125, 0.05, 0.025]]
    # priors = [0.25, 0.25, 0.25, 0.25]
    # archery = Bayes(hypos, priors, obs, likelihood)

    # Question 3: What is the probability that the archer is an intermediate level?
    # posterior = archery.compute_posterior(['yellow', 'white', 'blue', 'red', 'red', 'blue'])
    # print("The probability that the archer is an intermediate level is: %s" % posterior[1])

    # # Question 4: What is the most likely level of the archer?
    # most_likely_level_index = posterior.index(max(posterior))
    # print("The most likely level of the archer is: %s" % hypos[most_likely_level_index])
