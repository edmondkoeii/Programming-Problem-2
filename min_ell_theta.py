def learn_theta(data, colors):
    """
    Part (a): All blue points < all red points (no overlap).

    Returns a theta such that all blue points <= theta and all red points > theta.
    Optimal approach: find max blue and min red, return their midpoint.
    Time complexity: O(n)
    """
    max_blue = max(x for x, c in zip(data, colors) if c == 'blue')
    min_red = min(x for x, c in zip(data, colors) if c == 'red')
    return (max_blue + min_red) / 2


def compute_ell(data, colors, theta):
    """
    Part (b): Compute L(theta) = (# red points <= theta) + (# blue points > theta).
    Time complexity: O(n)
    """
    loss = 0
    for x, c in zip(data, colors):
        if c == 'red' and x <= theta:
            loss += 1
        elif c == 'blue' and x > theta:
            loss += 1
    return float(loss)


def minimize_ell(data, colors):
    """
    Part (c): Find a theta minimizing L(theta). Quadratic time complexity.

    Key insight: L(theta) only changes at data points, so we only need to
    check thetas between consecutive sorted data values. We try theta = each
    data point (which puts theta just at/after that value), checking all n
    candidate thresholds.
    Time complexity: O(n^2)
    """
    best_theta = None
    best_loss = float('inf')

    for theta in data:
        loss = compute_ell(data, colors, theta)
        if loss < best_loss:
            best_loss = loss
            best_theta = theta

    return float(best_theta)


def minimize_ell_sorted(data, colors):
    """
    Part (d): data is sorted. Find minimizing theta in linear time.

    Loop invariant: after the alpha-th iteration, blue_gt_theta is the number
    of blue points greater than data[alpha - 1].

    Initially (before any iteration), theta is conceptually -inf, so all blue
    points are > theta. As we sweep theta = data[0], data[1], ..., we update
    counts incrementally.

    L(theta) = red_le_theta + blue_gt_theta

    At theta = data[alpha]:
      - red_le_theta increases by 1 if data[alpha] is red
      - blue_gt_theta decreases by 1 if data[alpha] is blue
    Time complexity: O(n)
    """
    n = len(data)

    # Initially theta = -inf: no reds <= theta, all blues > theta
    red_le_theta = 0
    blue_gt_theta = sum(1 for c in colors if c == 'blue')

    best_loss = float('inf')
    best_theta = None

    for alpha in range(n):
        # Move theta to data[alpha]
        if colors[alpha] == 'red':
            red_le_theta += 1
        else:  # blue
            blue_gt_theta -= 1

        # Loop invariant holds: blue_gt_theta = # blue points > data[alpha]
        loss = red_le_theta + blue_gt_theta
        if loss < best_loss:
            best_loss = loss
            best_theta = data[alpha]

    return float(best_theta)
